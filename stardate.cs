// create a console app


using System;

namespace stardate
{
    class Program
    {
        static void Main(string[] args)
        {
            // prompt the user for a year
            Console.WriteLine("Enter a year: ");
            
            // read the user input
            string input = Console.ReadLine();

            // convert the input to an integer
            int year = Int32.Parse(input);

            // calculate the stardate
            double stardate = (year - 2323) * 1.025;

            // display the stardate
            Console.WriteLine("Stardate: " + stardate);

            // wait for user input before closing
            Console.ReadLine();                        
        }
    }
}
