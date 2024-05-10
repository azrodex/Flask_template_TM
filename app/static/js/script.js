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

// Attache l'événement "click" au bouton avec l'ID "generate-btn"
document.getElementById('generate-btn').addEventListener("click", genererCitation);

// Appelle la fonction pour générer une citation lors du chargement de la page
genererCitation()

// MENU BURGER 

document.addEventListener("DOMContentLoaded", function () {
    const menuHamburger = document.querySelector(".bx-menu");
    const navLinks = document.querySelector(".nav-links");

    menuHamburger.addEventListener('click', function(){
        navLinks.classList.toggle('mobile-menu')
    })
});




    







  
  
  
  
  
  
  
