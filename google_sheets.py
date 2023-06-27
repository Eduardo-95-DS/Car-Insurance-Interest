// P004 health insurance cross-sell

function onOpen(){
	var ui = SpreadsheetApp.getUi()
	ui.createMenu('Propensity Score')            # nome do menu
      .addItem('Get Prediction','PredictAll') # predictall é a função
      .addToUi();
}

host_production = 'health-insurance-model.herokuapp.com'   # MUDAR PARA O MEU APP 

// Helper Function
function ApiCall(data,endpoint){
	var url = 'https://' + host_production + endpoint;
	var payload = JSON.stringify(data);

	var options = {'method':'Post','contentType':'application/json','payload':payload};

	//Logger.log(url)
	//Logger.log(options)
	//adasdas

	var response = UrlFetchApp.fetch(url,options):

	//get response
	var rc = response.getResponseCode();
	var responseText = response.getContentText();

	if (rc !== 200){
		Logger.log('Response (%s) %s', rc, responseText);
	}

	else{
		prediction = JSON.parse(responseText);
	}

	return  prediction

};


//health insurance propensity score prediction
function PredictAll(){
	//google sheet parameters
	var ss = SpreadsheetApp.getActiveSheet();
	var titleColumns = ss.getRange('A1:L1').getValues()[0];     # colunas q serão transformadas em json
	var lastRow = ss.getLastRow();
																# objetivo final precisa ser uma lista de dicionários
	var data = ss.getRange('A2'+ ':' +'L' + lastRow).getValues();

	// run over all rows 
	for (row in data){                                   # row é uma variável q vai iterar dentro de data
		var json = new Object():                        # json é uma variável q representa o json da linha 

		// run over all collumns                         # cada iteração vai concatenar o come da coluna com a linha para criar o json
		for (var j=0; j < titleColumns.lenght; j++){     # j é a varíável de início e > é a condição de teste,j++ pra ir incrementando a variável
			json[titleColumns[j]] = data[row[j]];         # para cada título vai atribuir um valor  	
		};
	
	// list of json to send	
		var json_send = new Object();

		json_send['id'] 				= json['id']
		json_send['gender'] 			= json['gender']
		json_send['age'] 				= json['age']
		json_send['driving_license'] 	= json['driving_license']	
		json_send['region_code'] 		= json['region_code']
		json_send['previously_insured'] = json['previously_insured']
		json_send['vehicle_age'] 		= json['vehicle_age']
		json_send['vehicle_damage'] 	= json['vehicle_damage']
		json_send['annual_premium'] 	= json['annual_premium']
		json_send['policy_sales_channel'] = json['policy_sales_channel']
		json_send['vintage'] 			= json['vintage']
		json_send['response'] 			= json['response']
	


	//Logger.log(json_send);            # para ver a linha sem e com a predição
	//dfsdf

	pred = ApiCall(json_send,'/predict');

	//Logger.log(pred)

	//asdasd

	//send back to google sheets
	ss.getRange(Number(row)+2,13)setValue(pred[0]['score'])


	};
};