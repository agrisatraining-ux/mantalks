/**
 * Google Apps Script for ManTalks Automation
 * Instructions:
 * 1. Open your Google Sheet.
 * 2. Extensions > Apps Script.
 * 3. Delete any code and paste this.
 * 4. Update ADMIN_EMAIL with your email.
 * 5. Deploy > New Deployment > Web App.
 *    - Execute as: Me
 *    - Who has access: Anyone
 * 6. Copy the Web App URL and paste it into script.js
 */

const ADMIN_EMAIL = 'agrisatraining@gmail.com'; // Update this!
const WHATSAPP_LINK = 'https://wa.me/919840600638'; // Update this!

// Razorpay Live Keys
const RAZORPAY_KEY_ID = 'rzp_live_SYWYNjycdq6eQv';
const RAZORPAY_KEY_SECRET = 'mMEkvNOofvgUif0UzcuBpTsz';

function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);

    const ss = SpreadsheetApp.getActiveSpreadsheet();
    const sheet = ss.getSheetByName('Sheet1') || ss.getSheets()[0];

    // --- CASE 1: INITIATE (User clicked Submit, but hasn't paid yet) ---
    if (data.action === 'initiate') {
      const row = [
        data.displayName,
        data.email,
        data.phone,
        data.language,
        data.sessionType,
        data.date,
        data.timePref,
        'Initiated',  // Status
        'N/A'         // PaymentId
      ];
      sheet.appendRow(row);
      return ContentService.createTextOutput(JSON.stringify({ status: 'success' })).setMimeType(ContentService.MimeType.JSON);
    }
    
    // --- CASE 2: COMPLETE (User finished Razorpay) ---
    if (!data.paymentId || data.paymentId === 'N/A') {
      throw new Error("No payment ID provided during completion.");
    }

    // Verify Payment with Razorpay to ensure safe payment
    const rzpAuth = Utilities.base64Encode(RAZORPAY_KEY_ID + ':' + RAZORPAY_KEY_SECRET);
    const res = UrlFetchApp.fetch('https://api.razorpay.com/v1/payments/' + data.paymentId, {
      headers: {
        'Authorization': 'Basic ' + rzpAuth
      },
      muteHttpExceptions: true
    });
    const paymentInfo = JSON.parse(res.getContentText());

    if (paymentInfo.status !== 'captured' && paymentInfo.status !== 'authorized') {
      throw new Error('Invalid or unverified payment.');
    }

    // Attempt to update the existing row from "Initiated" to "PAID"
    const dataRange = sheet.getDataRange();
    const values = dataRange.getValues();
    let updatedIndex = -1;
    
    // Search backwards to safely find the most recent attempt
    for(let i = values.length - 1; i >= 0; i--) {
       if(values[i][1] === data.email) { // Email is Column B (index 1)
          updatedIndex = i + 1; // Row numbers are 1-indexed
          break;
       }
    }
    
    if (updatedIndex !== -1) {
       // Index 8 is Status ('PAID'), Index 9 is PaymentId
       sheet.getRange(updatedIndex, 8).setValue('PAID');
       sheet.getRange(updatedIndex, 9).setValue(data.paymentId);
    } else {
       // Failsafe: if we somehow couldn't find the row, append a new one
       sheet.appendRow([
         data.displayName, data.email, data.phone, data.language, 
         data.sessionType, data.date, data.timePref, 'PAID', data.paymentId
       ]);
    }

    // 2. Schedule Google Meet & Calendar Event
    const eventDetails = createCalendarEvent(data);

    // 3. Send Email Notifications
    sendEmails(data, eventDetails.meetLink);

    return ContentService.createTextOutput(JSON.stringify({
      status: 'success',
      whatsapp: WHATSAPP_LINK,
      meetLink: eventDetails.meetLink
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({
      status: 'error',
      message: err.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

function getTimeString(timePref) {
  // Maps the frontend's select options to actual times to prevent Invalid Date errors
  switch (timePref) {
    case 'Morning at 06:00 AM': return '06:00 AM';
    case 'Afternoon at 12:00 PM': return '12:00 PM';
    case 'Evening at 06:00 PM': return '06:00 PM';
    case 'Night at 09:00 PM': return '09:00 PM';
    default: return '09:00 AM';
  }
}

function createCalendarEvent(data) {
  // Parse date and time
  const timeString = getTimeString(data.timePref);
  const startTime = new Date(data.date + ' ' + timeString);
  const endTime = new Date(startTime.getTime() + (60 * 60 * 1000)); // +1 hour

  let meetLink = 'Link attached to Calendar invite';

  try {
    // IMPORTANT: This requires the "Calendar API" Advanced Service to be enabled in Apps Script!
    // (To enable: Go to Services (+) on the left panel -> Choose Google Calendar API -> Add)
    const calendarId = 'primary';
    const eventId = "mantalks" + new Date().getTime();

    const newEvent = {
      summary: 'ManTalks Session: ' + data.displayName,
      description: 'Session Type: ' + data.sessionType + '\nLanguage: ' + data.language,
      start: { dateTime: startTime.toISOString() },
      end: { dateTime: endTime.toISOString() },
      attendees: [
        { email: data.email },
        { email: ADMIN_EMAIL }
      ],
      conferenceData: {
        createRequest: {
          conferenceSolutionKey: { type: "hangoutsMeet" },
          requestId: eventId
        }
      }
    };

    // Insert event and request conference link creation
    const event = Calendar.Events.insert(newEvent, calendarId, {
      conferenceDataVersion: 1,
      sendUpdates: 'all'
    });

    // Extract Meet link from the created event
    if (event.conferenceData && event.conferenceData.entryPoints) {
      const entryPoint = event.conferenceData.entryPoints.find(ep => ep.entryPointType === 'video');
      if (entryPoint) {
        meetLink = entryPoint.uri;
      }
    }
  } catch (e) {
    // Fallback if the Advanced Calendar Service is disabled
    const calendar = CalendarApp.getDefaultCalendar();
    calendar.createEvent(
      'ManTalks Session: ' + data.displayName,
      startTime,
      endTime,
      {
        description: 'Session Type: ' + data.sessionType + '\nLanguage: ' + data.language + '\n\nNote: Please add a Meet link manually if missing.',
        guests: data.email + ',' + ADMIN_EMAIL,
        sendInvites: true
      }
    );
    console.error("Advanced Calendar Service not enabled or failed:", e);
  }

  return { meetLink: meetLink };
}

function sendEmails(data, meetLink) {
  // To User
  const userSubject = 'Welcome to ManTalks! Your session is confirmed';
  const userBody = `Hi ${data.displayName},\n\nYour payment of 399 INR was successful. Your session is scheduled for ${data.date} during ${data.timePref} slot.\n\nA Google Meet link has been added to your calendar.\n\nFor any queries, contact us here: ${WHATSAPP_LINK}\n\nWelcome to the circle!`;

  MailApp.sendEmail(data.email, userSubject, userBody);

  // To Admin
  const adminSubject = 'New PAID User: ' + data.displayName;
  const adminBody = `A new user has paid 399 INR.\n\nName: ${data.displayName}\nEmail: ${data.email}\nPhone: ${data.phone}\nLevel/Session: ${data.sessionType}\nTime: ${data.date} at ${data.timePref}`;

  MailApp.sendEmail(ADMIN_EMAIL, adminSubject, adminBody);
}
