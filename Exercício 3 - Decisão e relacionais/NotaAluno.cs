using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Nota
{
	public class Program
	{
		public static void Main(string[] args)
		{
			Console.WriteLine("Digite a nota: \n");
			string nota = Console.ReadLine();
			double notatrue = double.Parse(nota);
			
			if(notatrue <= 5) {
			  Console.WriteLine("Reprovado.");
			}
			else if(notatrue > 5 && notatrue <= 6) {
			  Console.WriteLine("Recuperação.");
			}
			else {
			  Console.WriteLine("Aprovado");
			}
		}
	}
}