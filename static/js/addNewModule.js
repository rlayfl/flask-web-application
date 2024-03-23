// Kaplan demonstration code

//The following submit event handler is ONE way of handling form submissions. There are many ways of doing it but this is 
//how I like to handle it.

//The caveat here is that we're not doing this in a function but instead applying a submit event handler to the form. 
//You could do this with a function if you preferred

//When the addNewModuleForm form is submitted
$("#addNewModuleForm").on("submit", function(event) {
    event.preventDefault()
  
    //We initialise a blank javascript object to populate with the form values
    var addNewModule = {
      code: null,
      name: null,
      description: null,
      startDate: null,
      endDate: null
    }
  
    //For each of the form input fields
    $(this).find("input, textarea").each(function(){
  
      //What we are doing here is checking if the current form input is called "code".
      //If it is called "code", we assign the value of addNewModule object's code as the value in the form field
      if ($(this).prop("name") == "code") {
        addNewModule.code = $(this).val();
      }
  
      //Do the same for the other values
      if ($(this).prop("name") == "name") {
        addNewModule.name = $(this).val();
      }
  
      if ($(this).prop("name") == "description") {
        addNewModule.description = $(this).val();
      }
  
      if ($(this).prop("name") == "startDate") {
        addNewModule.startDate = $(this).val();
      }
  
      if ($(this).prop("name") == "endDate") {
        addNewModule.endDate = $(this).val();
      }
  
    })
  
    //Now, we turn the completed object into a JSON object for use with ajax call to the server
    var JSONFormData = JSON.stringify(addNewModule)
  
    console.log("Testing database");
  
    $.ajax({
        type: "POST",
        url: "/addNewModule",
        contentType: "application/json; charset=utf-8",
        data: {
            addNewModuleJSONObject: JSONFormData
        },
        success: function (data) {
            alert("Success")
        },
        error: function (data) {
            alert(JSON.stringify(data))
            alert("Error while adding new module");
        }
    })
  })
  
  
  