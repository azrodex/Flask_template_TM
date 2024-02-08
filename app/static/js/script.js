console.log("Script bien chargé")

// verifiaction du mdp
function ConfirmPasswords() {
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirm-password").value;

    if (password !== confirmPassword) {
      alert("Les mots de passe ne correspondent pas !");
      return false;
    }

    return true;
}

// scroll

document.addEventListener("DOMContentLoaded", function () {
  const scrollLinks = document.querySelectorAll(".scroll-link");

  function scrollToSection(event) {
      event.preventDefault();

      const targetId = event.currentTarget.getAttribute("href").substring(1);
      const targetSection = document.getElementById(targetId);

      if (targetSection) {
          const offset = 130;
          window.scrollTo({
              top: targetSection.offsetTop - offset,
              behavior: "smooth",
          });
      }
  }

  scrollLinks.forEach(function (link) {
      link.addEventListener("click", scrollToSection);
  });

})

// CITATION

const Quotes = [
    { quote: "La vie est ce qui arrive pendant que vous êtes occupé à faire d'autres projets.", author: "Allen Sanders" },
    { quote: "Le seul endroit où le succès vient avant le travail est dans le dictionnaire.", author: "Vidal Sassoon" },
    { quote: "La vie est vraiment simple, mais nous insistons à la rendre compliquée.", author: "Confucius" },
    { quote: "L'échec est le condiment qui donne sa saveur au succès.", author: "Truman Capote" },
    { quote: "La seule façon de faire du bon travail est d'aimer ce que vous faites.", author: "Steve Jobs" },
    { quote: "La seule chose que nous ayons à craindre, c'est la peur elle-même.", author: "Franklin D. Roosevelt" },
    { quote: "La vie n'est pas attendre que l'orage passe, c'est apprendre à danser sous la pluie.", author: "Sénèque" },
    { quote: "La folie, c'est se comporter de la même manière et s'attendre à un résultat différent.", author: "Albert Einstein" },
    { quote: "L'éducation est l'arme la plus puissante que vous pouvez utiliser pour changer le monde.", author: "Nelson Mandela" },
    { quote: "La meilleure façon de prédire l'avenir est de le créer.", author: "Peter Drucker" },
    { quote: "Soyez le changement que vous voulez voir dans le monde.", author: "Mahatma Gandhi" },
    { quote: "La vie commence là où la peur s'arrête.", author: "Osho" },
    { quote: "L'amour ne se voit pas avec les yeux mais avec l'âme.", author: "William Shakespeare" },
    { quote: "La véritable éducation consiste à tirer le meilleur de soi-même. Quel meilleur livre peut-il exister que le livre de l'humanité ?", author: "Gandhi" },
    { quote: "Il n'y a qu'une chose qui rend un rêve impossible à réaliser : la peur de l'échec.", author: "Paulo Coelho" },
    { quote: "La plus grande gloire n'est pas de ne jamais tomber, mais de se relever à chaque chute.", author: "Confucius" },
    { quote: "La vie n'est pas d'attendre que l'orage passe, mais d'apprendre comment danser sous la pluie.", author: "Sénèque" },
    { quote: "La liberté est le droit de faire ce que les lois permettent.", author: "Montesquieu" },
    { quote: "La vie est une fleur dont l'amour est le miel.", author: "Victor Hugo" },
    { quote: "On ne voit bien qu'avec le cœur. L'essentiel est invisible pour les yeux.", author: "Antoine de Saint-Exupéry" },
    { quote: "La vie, c'est comme une bicyclette, il faut avancer pour ne pas perdre l'équilibre.", author: "Albert Einstein" },
    { quote: "Il n'y a pas de vent favorable pour celui qui ne sait pas où il va.", author: "Sénèque" },
    { quote: "Le bonheur n'est pas une destination à atteindre, mais une manière de voyager.", author: "Margaret Lee Runbeck" },
    { quote: "Le plus grand secret du bonheur, c'est d'être bien avec soi.", author: "Bernard Fontenelle" },
    { quote: "Le succès n'est pas la clé du bonheur. Le bonheur est la clé du succès. Si vous aimez ce que vous faites, vous réussirez.", author: "Albert Schweitzer" },
    { quote: "La confiance en soi est le premier secret du succès.", author: "Ralph Waldo Emerson" },
    { quote: "Le succès, c'est d'aller d'échec en échec sans perdre son enthousiasme.", author: "Winston Churchill" },
    { quote: "La vie est un mystère qu'il faut vivre, et non un problème à résoudre.", author: "Gandhi" },
    { quote: "Le plus grand risque dans la vie, c'est de ne pas en prendre.", author: "Robert Kennedy" },
    { quote: "La vie, c'est comme une bicyclette, pour garder l'équilibre, il faut avancer.", author: "Albert Einstein" },
    { quote: "Le bonheur n'est pas quelque chose que l'on possède, c'est quelque chose que l'on fait.", author: "André Maurois" },
    { quote: "La seule façon de faire du bon travail est d'aimer ce que vous faites.", author: "Steve Jobs" },
    { quote: "La vie devient ce que l'on en fait.", author: "Confucius" },
    { quote: "Rien n'est impossible, il suffit de le vouloir.", author: "Alexandre le Grand" },
    { quote: "Il n'y a pas de hasards, il n'y a que des rendez-vous.", author: "Paul Eluard" },
    { quote: "La seule façon dont les choses peuvent changer pour le mieux, c'est lorsque vous changez pour le mieux. On ne souhaite pas quelque chose de meilleur, on le devient.", author: "Jim Rohn" },
    { quote: "La véritable sagesse consiste à savoir que l'on ne sait rien.", author: "Socrate" },
    { quote: "Le talent, c'est l'envie de faire quelque chose.", author: "Jacques Brel" },
    { quote: "La vie est courte, l'art est long, l'occasion fugitive, l'expérience trompeuse, le jugement difficile.", author: "Hippocrate" },
    { quote: "L'avenir appartient à ceux qui croient en la beauté de leurs rêves.", author: "Eleanor Roosevelt" },
    { quote: "Si vous voulez le bonheur d'une heure, prenez une sieste. Si vous voulez le bonheur d'une journée, allez à la pêche. Si vous voulez le bonheur d'une année, héritez d'une fortune. Si vous voulez le bonheur d'une vie, aidez quelqu'un d'autre.", author: "Proverbe chinois" },
    { quote: "Le succès, c'est d'obtenir ce que l'on veut. Le bonheur, c'est aimer ce que l'on obtient.", author: "H. Jackson Brown" },
    { quote: "La beauté de la vie réside dans l'inattendu.", author: "Antoine de Saint-Exupéry" },
    { quote: "La vie est faite de choix. Osez faire celui qui vous rendra heureux.", author: "Albert Camus" },
    { quote: "Ne laissez pas le comportement des autres détruire votre paix intérieure.", author: "Dalai Lama" },
    { quote: "La seule limite à notre épanouissement de demain sera nos doutes d'aujourd'hui.", author: "Franklin D. Roosevelt" },

  ];

function genererCitation() {
    const indiceAleatoire = Math.floor(Math.random() * Quotes.length);
    const { quote, author } = Quotes[indiceAleatoire];

    const quotesElement = document.getElementById('citation');

    quotesElement.innerHTML = `"${quote}"<br><span class="auteur">${author}</span></br>`;
}

document.getElementById('generate-btn').addEventListener('click', genererCitation);

genererCitation();

// MENU BURGER 

document.addEventListener("DOMContentLoaded", function () {
    const menuHamburger = document.querySelector(".bx-menu");
    const navLinks = document.querySelector(".nav-links");

    menuHamburger.addEventListener('click', function(){
        navLinks.classList.toggle('mobile-menu')
    })
});


document.addEventListener('DOMContentLoaded', function(){
    var today = new Date(),
        year = today.getFullYear(),
        month = today.getMonth(),
        monthTag =["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
        day = today.getDate(),
        days = document.getElementsByTagName('td'),
        selectedDay,
        setDate,
        daysLen = days.length;
// options should like '2014-01-01'
    function Calendar(selector, options) {
        this.options = options;
        this.draw();
    }
    
    Calendar.prototype.draw  = function() {
        this.getCookie('selected_day');
        this.getOptions();
        this.drawDays();
        var that = this,
            reset = document.getElementById('reset'),
            pre = document.getElementsByClassName('pre-button'),
            next = document.getElementsByClassName('next-button');
            
            pre[0].addEventListener('click', function(){that.preMonth(); });
            next[0].addEventListener('click', function(){that.nextMonth(); });
            reset.addEventListener('click', function(){that.reset(); });
        while(daysLen--) {
            days[daysLen].addEventListener('click', function(){that.clickDay(this); });
        }
    };
    
    Calendar.prototype.drawHeader = function(e) {
        var headDay = document.getElementsByClassName('head-day'),
            headMonth = document.getElementsByClassName('head-month');

            e?headDay[0].innerHTML = e : headDay[0].innerHTML = day;
            headMonth[0].innerHTML = monthTag[month] +" - " + year;        
     };
    
    Calendar.prototype.drawDays = function() {
        var startDay = new Date(year, month, 1).getDay(),
//      下面表示这个月总共有几天
            nDays = new Date(year, month + 1, 0).getDate(),
    
            n = startDay;
//      清除原来的样式和日期
        for(var k = 0; k <42; k++) {
            days[k].innerHTML = '';
            days[k].id = '';
            days[k].className = '';
        }

        for(var i  = 1; i <= nDays ; i++) {
            days[n].innerHTML = i; 
            n++;
        }
        
        for(var j = 0; j < 42; j++) {
            if(days[j].innerHTML === ""){
                
                days[j].id = "disabled";
                
            }else if(j === day + startDay - 1){
                if((this.options && (month === setDate.getMonth()) && (year === setDate.getFullYear())) || (!this.options && (month === today.getMonth())&&(year===today.getFullYear()))){
                    this.drawHeader(day);
                    days[j].id = "today";
                }
            }
            if(selectedDay){
                if((j === selectedDay.getDate() + startDay - 1)&&(month === selectedDay.getMonth())&&(year === selectedDay.getFullYear())){
                days[j].className = "selected";
                this.drawHeader(selectedDay.getDate());
                }
            }
        }
    };
    
    Calendar.prototype.clickDay = function(o) {
        var selected = document.getElementsByClassName("selected"),
            len = selected.length;
        if(len !== 0){
            selected[0].className = "";
        }
        o.className = "selected";
        selectedDay = new Date(year, month, o.innerHTML);
        this.drawHeader(o.innerHTML);
        this.setCookie('selected_day', 1);
        
    };
    
    Calendar.prototype.preMonth = function() {
        if(month < 1){ 
            month = 11;
            year = year - 1; 
        }else{
            month = month - 1;
        }
        this.drawHeader(1);
        this.drawDays();
    };
    
    Calendar.prototype.nextMonth = function() {
        if(month >= 11){
            month = 0;
            year =  year + 1; 
        }else{
            month = month + 1;
        }
        this.drawHeader(1);
        this.drawDays();
    };
    
    Calendar.prototype.getOptions = function() {
        if(this.options){
            var sets = this.options.split('-');
                setDate = new Date(sets[0], sets[1]-1, sets[2]);
                day = setDate.getDate();
                year = setDate.getFullYear();
                month = setDate.getMonth();
        }
    };
    
     Calendar.prototype.reset = function() {
         month = today.getMonth();
         year = today.getFullYear();
         day = today.getDate();
         this.options = undefined;
         this.drawDays();
     };
    
    Calendar.prototype.setCookie = function(name, expiredays){
        if(expiredays) {
            var date = new Date();
            date.setTime(date.getTime() + (expiredays*24*60*60*1000));
            var expires = "; expires=" +date.toGMTString();
        }else{
            var expires = "";
        }
        document.cookie = name + "=" + selectedDay + expires + "; path=/";
    };
    
    Calendar.prototype.getCookie = function(name) {
        if(document.cookie.length){
            var arrCookie  = document.cookie.split(';'),
                nameEQ = name + "=";
            for(var i = 0, cLen = arrCookie.length; i < cLen; i++) {
                var c = arrCookie[i];
                while (c.charAt(0)==' ') {
                    c = c.substring(1,c.length);
                    
                }
                if (c.indexOf(nameEQ) === 0) {
                    selectedDay =  new Date(c.substring(nameEQ.length, c.length));
                }
            }
        }
    };
    var calendar = new Calendar();
    
        
}, false);
    







  
  
  
  
  
  
  
