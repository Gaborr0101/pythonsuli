using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace fealdat1
{
    internal class adatok
    {
        public int kezd;
        public int veg;
        public string szin;
        public int sorszam;

        public adatok(string sor, int sorszam)
        {
            string[] vag = sor.Split(" ");
            kezd = int.Parse(vag[0]);
            veg = int.Parse(vag[1]);
            szin = vag[2];
            this.sorszam = sorszam;
        }

        public bool kaputKetOldal
        {
            get
            {
                return kezd > veg;
            }
        }

        public bool benneVanEz(int sorszam)
        {
            return (sorszam >= kezd && sorszam <= veg)
                || (kaputKetOldal && (kezd <= sorszam || veg >= sorszam));
        }
    }
}