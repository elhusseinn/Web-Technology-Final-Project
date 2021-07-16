function validate(){
    var field1 = document.getElementById('id_new_password1');
    var field2 = document.getElementById('id_new_password2');
    if (!field1) field1 = document.getElementById('id_password1');
    if (!field2) field2 = document.getElementById('id_password2');
    
    if (field1.value != field2.value){
        document.getElementById("hdn").style.display = "block";
    }
    else{
        document.getElementById("hdn").style.display = "none";
    }
}



var elementEV = document.getElementById('id_new_password2');
if (!elementEV) elementEV = document.getElementById('id_password2');
elementEV.addEventListener("input", validate);
