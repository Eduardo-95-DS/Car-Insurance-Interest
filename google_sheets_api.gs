// PA004 Health Insurance Cross-sell
function onOpen() {
  var ui = SpreadsheetApp.getUi();
  ui.createMenu( 'Health Insurance Prediction' )
    .addItem( 'Get Prediction', 'PredictAll')
    .addToUi();  
}

// Production Server
host_production = 'car-insurance-interest.onrender.com'

// ----------------------------
// ----- Helper Function ------
// ----------------------------
// API Call
function ApiCall( data, endpoint ){
  var url = 'https://' + host_production + endpoint;
  var payload = JSON.stringify( data );

  var options = {'method': 'POST', 'contentType': 'application/json', 'payload': payload};

  Logger.log( url )
  Logger.log( options )

  var response = UrlFetchApp.fetch( url, options );

  // get response
  var rc = response.getResponseCode();
  var responseText = response.getContentText();

  if ( rc !== 200 ){
    Logger.log( 'Response (%s) %s', rc, responseText );
  }
  else{
    prediction = JSON.parse( responseText );
  }
  return prediction
};

// Health Insurance Propensity Score Prediction
function PredictAll(){
  //google sheets parameters
  var ss = SpreadsheetApp.getActiveSheet();
  var titleColumns = ss.getRange( 'A1:L1' ).getValues()[0];
  var lastRow = ss.getLastRow();
  
  var data = ss.getRange( 'A2' + ':' + 'L' + lastRow ).getValues();

  // run over all rows
  for ( row in data ){
    var json = new Object();

    // run over all columns
    for( var j=0; j < titleColumns.length; j++ ){
      json[titleColumns[j]] = data[row][j];
    };

    // Json file to send
    var json_send = new Object();
    json_send['id'] = json['id']
    json_send['Gender'] = json['Gender']
    json_send['Age'] =  json['Age']
    json_send['Driving_License'] = json['Driving_License']
    json_send['Region_Code'] = json['Region_Code']
    json_send['Previously_Insured'] = json['Previously_Insured']
    json_send['Vehicle_Age'] = json['Vehicle_Age']
    json_send['Vehicle_Damage'] = json['Vehicle_Damage']
    json_send['Annual_Premium'] = json['Annual_Premium']
    json_send['Policy_Sales_Channel'] = json['Policy_Sales_Channel']
    json_send['Vintage'] = json['Vintage']
    // json_send['response'] = json['response']

    // Propensity score
    pred = ApiCall( json_send, '/predict' );

    // Send back to google sheets
    ss.getRange( Number( row ) + 2 , 13 ).setValue( pred[0]['score'] )
    Logger.log( pred[0]['score'] )
    Logger.log( row )
  };
};

