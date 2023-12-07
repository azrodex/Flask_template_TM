console.log("Script bien chargé")

function ConfirmPasswords() {
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirm-password").value;

    if (password !== confirmPassword) {
      alert("Les mots de passe ne correspondent pas !");
      return false;
    }

    return true;
}


// function validate() { 
//     var msg; 
//     var str = document.getElementById("password").value; 
//     if (str.match( /[0-9]/g) && 
//             str.match( /[A-Z]/g) && 
//             str.match(/[a-z]/g) && 
//             str.match( /[^a-zA-Z\d]/g) &&
//             str.length >= 10) 
//         msg = "<p style='color:green'>Mot de passe fort.</p>"; 
//     else 
//         msg = "<p style='color:red'>Mot de passe faible.</p>"; 
//     document.getElementById("msg").innerHTML= msg; 
// }