// Compile Template
var source = $("#project-template").html();
var projectTemplate = Handlebars.compile(source);

// Loop through data and display content 
var content = "";
for (var i in data) {
    content += projectTemplate(data[i]);
}

// Add the navbar content to the page
$("#ward-info").html(content);