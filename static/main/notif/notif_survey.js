setInterval(function(){
    $.get('/api/notification/survey/',function(data) {
        document.getElementById("notifsurvey").innerHTML = data.value;
    });
}, 5000);
console.log(data.value)