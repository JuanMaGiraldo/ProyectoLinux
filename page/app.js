// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(loadCharts);

// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.
function loadCharts(){
  text = readTextFile("../scripts/report.txt")
  removeItem(text,"");
  removeItem(text,"\n");
  while(text.length != 0){
    text = getData(text);
  }  
}

function getData(text){
  title = text.shift();
  summary = text.shift();
  name = text.shift();
  value = text.shift();
  type = text.shift();
  data = []
  while(text[0] != "fin"){
    data.push([text.shift(),parseFloat(text.shift())]);
  }  
  createDivInfo(title,summary,name, value, data,type);
  text.shift();
  return text;
}

function createDivInfo(title,summary,name, value, data,type){
  divs = createCard(title,summary);
  createTable(name, value, data,divs[0]);
  createChart(name, value, data,type,divs[1]);
}


function createChart(name, value, dataTable, type,div) {

  // Create the data table.
  var data = new google.visualization.DataTable();
  data.addColumn('string', name);
  data.addColumn('number', value);
  data.addRows(dataTable);
  
  var options = {'width':500,
                 'height':300}; 
  drawChart(type,data,options,div);
}

function drawChart(type, data, options, div){
  var chart = null;
  type = type.toUpperCase();
  // Instantiate and draw our chart, passing in some options. 
  switch(type){
      case "PIE":
          chart = new google.visualization.PieChart(div);
          break;
      case "BAR":
          chart = new google.visualization.BarChart(div);
          break;
      case "SCATTER":
          chart = new google.visualization.ScatterChart(div);
          break;
      case "AREA":
          chart = new google.visualization.AreaChart(div);
          break;
  }        
  chart.draw(data, options);  
}

function createCard(title, summary){
  var divCard = createDiv();
  divCard.className  = "card div-center";  
  var divTitle = createDiv();
  divTitle.className = "card-header bg-primary";
  divTitle.innerHTML = title.toUpperCase();
  var divBody = createDiv();
  divBody.className = "card-body";

  var divSummary = createDiv();
  divSummary.innerHTML = summary;
  divSummary.className = "div-summary";
  divBody.appendChild(divSummary);

  var divTable = createDiv();
  divTable.className = "div-table";
  var divChart = createDiv();
  divChart.className = "div-chart";

  
  
  divBody.appendChild(divTable);
  divBody.appendChild(divChart); 

  divCard.appendChild(divTitle);
  divCard.appendChild(divBody);
  document.getElementById("container").appendChild(divCard);
  
  return [divTable,divChart];
}

function createDiv(){
  return createElement("div");
}

function createTable(name, value, dataTable,div){
  var table = createElement("table");
  table.className = "table";
  //create header
  var header = createElement('thead');
  header.className = "thead-dark";
  var trHeader = createElement("tr");

  var top = ["#",name,value];
  for(let item of top){
    var th = createElement("th");
    th.scope = "col";
    th.innerHTML = item;
    trHeader.appendChild(th);
  }
  header.appendChild(trHeader);
  table.appendChild(header);

  //create body
  var tbdy = createElement('tbody');
  var i = 1;
  for(let row of dataTable){
    tr = createElement("tr");
    th = createElement("th");
    th.innerHTML = i;    
    th.scope = "row";    
    tr.appendChild(th);
    tr.appendChild(createTd(row[0]));
    tr.appendChild(createTd(row[1]));
    tbdy.appendChild(tr);
    i++;
  }
  
  table.appendChild(tbdy);
  div.appendChild(table);
} 

function createTd(value){
  td = createElement("td");
  td.innerHTML = value;
  return td;
}

function createElement(element){
  return document.createElement(element);
}

function readTextFile(file)
{
    var rawFile = new XMLHttpRequest();
    var allText;
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                allText = rawFile.responseText;
            }
        }
    }
    rawFile.send(null);
    return allText.split("\n");
}

function removeItem(array, item) {
  var i = array.length;

  while (i--) {
      if (array[i] === item) {
          array.splice(array.indexOf(item), 1);
      }
  }
}