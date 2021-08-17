public


class Date {
private final int[]nbJours=
{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
private int jour, mois, annee;

public Date(int jour, int mois, int annee) throws Exception{
this.jour = jour;
this.mois = mois;
this.annee = annee;
verifierValidite();
}

public boolean estBissextile(){


return (annee % 4 == 0 & & annee % 100 != 0) | | annee % 400 == 0;
}

public
boolean
equals(Object
o){
if (o instanceof Date){
Date d = (Date) o;
return jour == d.jour & & mois == d.mois & & annee == d.annee;
} else return false;
}

/ **
*Retourne
un
nombre
négatif
si
la
date
this
est
avant
o,
*un
nombre
positif
si
this
est
après
o,
*et
0
si
les
deux
dates
sont
égales.
* @ param
o
doit
être
une
date
* @
return
* @ exception
ClassCastException
si
o
n
'est pas une date
** /
public
int
compareTo(Object
o) {
    Date
d = (Date)
o;
return jourJulien() - d.jourJulien();
}

private
void
verifierValidite()
throws
DateException
{
if (mois < 0 | | mois > 12)throw new DateException("mois illégal");
if ((mois == 2 & & estBissextile() & & jour > 0 & & jour <= 29) | |
        (jour > 0 & & jour <= nbJours[mois - 1]));
else throw new DateException("jour de mois illégal");
}


public
int
jourJulien()
{
// numérotation
des
jours
à
partir
du
lundi
1
janvier - 4712
à
12
h
// (Joseph Juste Scaliger 1583)
// conversion
à
partir
du
calendrier
grégorien
// algo
de
l´Institut
de
mécanique
céleste
et
de
calcul
des
éphémérides
int
heures = 12;
int
GGG = 1;
if (annee < 1582) GGG = 0;
if (annee <= 1582 & & mois < 10) GGG = 0;
if (annee <= 1582 & & mois == 10 & & jour < 5) GGG = 0;
double
JD = -1 * Math.floor(7 * (Math.floor((mois + 9) / 12.) + annee) / 4.);
int
S = 1;
if ((mois - 9) < 0) S=-1;
int
A = Math.abs(mois - 9);
double
J1 = Math.floor(annee + S * Math.floor(A / 7.));
J1 = -1 * Math.floor((Math.floor(J1 / 100) + 1) * 3 / 4.);
JD = JD + Math.floor(275 * mois / 9.) + jour + (GGG * J1);
JD = Math.floor(JD + 1721027 + 2 * GGG + 367 * annee - 0.5);
JD = JD + (heures / 24.);
if (JD < 0) JD = 0;
return (int)
Math.round(JD);
}

public
String
jourSemaine()
{
int
jj = jourJulien();
switch((int)(jj + 1.5) % 7)
{
    case
0:
return "dimanche";
case
1:
return "lundi";
case
2:
return "mardi";
case
3:
return "mercredi";
case
4:
return "jeudi";
case
5:
return "vendredi";
default:
return "samedi";
}
}

public
int
getJour()
{
return jour;}

public
int
getMois()
{
return mois;}

public
String
getMoisChaine()
{
switch(mois)
{
    case
1:
return "janvier";
case
2:
return "février";
case
3:
return "mars";
case
4:
return "avril";
case
5:
return "mai";
case
6:
return "juin";
case
7:
return "juillet";
case
8:
return "août";
case
9:
return "septembre";
case
10:
return "octobre";
case
11:
return "novembre";
case
12:
default:
return "décembre";
}
}

public
int
getAnnee()
{
return annee;}

public
void
jourSuivant()
{
try{
++jour;
verifierValidite();
}catch(DateException ex){
try{
++mois;
jour = 1;
verifierValidite();
}catchDate(Exception ex1){
try{
++annee;
jour = 1;
mois = 1;
verifierValidite();
}catch(DateException ex2){}
}
}
}


public
void
jourPrecedent()
{
try{
--jour;
verifierValidite();
}catch(DateException ex){
try{
--mois;
jour = nbJours[mois - 1];
if (estBissextile() & & mois == 2)++jour;
verifierValidite();
}catch(DateException ex1){
try{
--annee;
jour = 31;
mois = 12;
verifierValidite();
}catch(DateException ex2){}
}
}
}

public
int
quantieme()
{ // numéro
du
jour
dans
l
'année
return !estBissextile()
? (int)(Math.round(275 * mois / 9 - 2 * Math.round((mois + 9) / 12)) + jour - 30)
: (int)(Math.round(275 * mois / 9 - Math.round((mois + 9) / 12)) + jour - 30);
}


public
String
toString()
{
return d.jourSemaine() + " " + d.getJour() + " " +
d.getMoisChaine() + " " + d.getAnnee();
}

}