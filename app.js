// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(loadCharts);

// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.
function loadCharts(){
  data= [
    ['Mushrooms', 3],
    ['Onions', 1],
    ['Olives', 1],
    ['Zucchini', 1],
    ['Pepperoni', 2]
  ];
  drawChart("Datos de ....","estos es...","Topping","Slices", data,"Bar" ,1);
  drawChart("Datos de ....","estos es...","Topping","Slices", data,"Pie" ,2);
}


function drawChart(title, resume, name, value, dataTable, type, id) {

  // Create the data table.
  var data = new google.visualization.DataTable();
  data.addColumn('string', name);
  data.addColumn('number', value);
  data.addRows(dataTable);
  
  var options = {'title':'How Much Pizza I Ate Last Night',
                 'width':500,
                 'height':300};
  
  var div = document.createElement("div");
  div.className  = "divInfo";  
  document.getElementById("container").appendChild(div);
  var chart = null;
  // Instantiate and draw our chart, passing in some options. 
  switch(type){
      case "Pie":
          chart = new google.visualization.PieChart(div);
          break;
      case "Bar":
          chart = new google.visualization.BarChart(div);
          break;
  }        
  chart.draw(data, options);
}