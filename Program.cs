namespace fealdat1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string[] sorok = File.ReadAllLines("felajanlas.txt");
            List<adatok> felajanlasok = new List<adatok>();
            int agyasDb = int.Parse(sorok[0]);

            for (int i = 1; i < sorok.Length; i++)
            {
                felajanlasok.Add(new adatok(sorok[i], i));
            }
            Console.WriteLine($"2. feladat:\nA felajanlasok száma: {felajanlasok.Count}");

            Console.WriteLine("3. feladat");

            Console.WriteLine("4. feladat");
            Console.Write("Adja meg az ágyás sorszámát! ");
            int agyas = int.Parse(Console.ReadLine());
            int darab = 0;
            string szin = "#";
            List<string> szinek = new List<string>();
            for (int i = 0; i < felajanlasok.Count; i++)
            {
                if (felajanlasok[i].benneVanEz(agyas))
                {
                    darab++;
                    if (darab == 1)
                    {
                        szin = felajanlasok[i].szin;
                    }
                    if (!szinek.Contains(felajanlasok[i].szin))
                    {
                        szinek.Add(felajanlasok[i].szin);
                    }
                }
            }
            Console.WriteLine("A felajánlók száma: {0}", darab);
            Console.WriteLine("A virágágyás szine, ha csak az első ültet: {0}", szin);
            Console.WriteLine("A virágágyás színei: {0}", String.Join(" ", szinek));

            int ures =0
            for (int i = 1; i <= agyasDb; i++) {
            
                darab=0;
                for (int k = 0; k <= felajanlasok.Count; k++) {
                    if (felajanlasok[k].benneVanEz(i))
                    {

                    darab++; }}
                
                
                }
                if (darab == 0)
                {
                ures++;
                }

            if (ures == 0) {
            Console.WriteLine()
                    }


            }


            Console.ReadKey();
        }
    }
}