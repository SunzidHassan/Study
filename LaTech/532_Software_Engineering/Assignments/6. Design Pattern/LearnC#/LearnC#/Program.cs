using System.Net.NetworkInformation;

namespace learnCS
{
    class Program
    {
        static void Main(string[] args)
        {
            string characterName = "John";
            char initial = 'A';
            int characterAge = 10;
            double gpa = 3.5;
            bool isMale = true;

            Console.WriteLine("There was a man named " + initial + ". " + characterName);
            Console.WriteLine("He was " + characterAge + " years old");
            Console.WriteLine("His GPA was: " + gpa);

            Console.ReadLine();
        }
    }
}