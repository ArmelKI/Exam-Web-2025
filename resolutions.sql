PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Resolutions" (
"Id"INTEGER NOT NULL UNIQUE,
"Title"TEXT NOT NULL,
"Description"TEXT NOT NULL,
"ImagePath"TEXT,
"Achieved" BOOLEAN DEFAULT false,
PRIMARY KEY("Id")
);
INSERT INTO Resolutions VALUES(1,'Faire plus d''exercice','Se remettre en forme avec des activités régulières','images/exercise.jpg',0);
INSERT INTO Resolutions VALUES(2,'Apprendre une nouvelle compétence','Élargir ses horizons avec une compétence utile','images/skill.jpg',0);
INSERT INTO Resolutions VALUES(3,'Voyager davantage','Explorer de nouveaux horizons et cultures','images/travel.jpg',0);
INSERT INTO Resolutions VALUES(5,'Passer plus de temps avec ses proches','Renforcer les liens familiaux et amicaux','images/family.jpg',1);
INSERT INTO Resolutions VALUES(42,'Économiser plus','Planifier un avenir financier sûr','images/savings.jpg',0);
INSERT INTO Resolutions VALUES(43,'Prendre le temps de ralentir et de cultiver son bien-être intérieur','Incorporer la relaxation et le yoga dans sa routine quotidienne pour réduire le stress et atteindre une meilleure sérénité et une plus grande harmonie mentale et physique','images/relax.jpg',1);
COMMIT;
