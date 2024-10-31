$(document).ready(function(){
  $("#submitBtn").click(function(e){
    e.preventDefault(); // prevent default form submission
    var formData = $("#myForm").serialize(); // get form data
    $.ajax({
      url: "bbxaudiomainpage.php",
      type: "POST",
      data: formData,
      success: function(response){
        // handle success response
        console.log(response);
      },
      error: function(xhr, status, error){
        // handle error response
        console.log(xhr.responseText);
      }
    });
  });
});
