using System;
using System.Diagnostics;
using System.Formats.Asn1;

namespace HD_Warren__403Final_
{
	class Program
	{
		static void Main(string[] args)
		{
			/*
			provide a comparison of the four approaches to mod division from the problem statement
			using visual studio's cpu and memory tools.
			*or paste into your c# ide of choice that has memory and compute profiling tools and use those
			
			note their performances will be very similar or different depending on your operands.

			i don't care how you do it, but you need to make a bunch of function and operator calls.
			eg. try small and large operands -- maybe loop through some operands, or handcode inputs at different scales.
			
			pit these methods against one another and profile them.
			provide a meaningful comparison of the performance of the four approaches
			in terms of memory and cpu usage.
			
			*/

			//
			Program p = new Program();

			/////////////////////////////////////////
			//your method calls here


			p.ModBIter(15, 10);
			p.ModDIter(15, 10);
			p.ModOIter(15, 10);
			p.ModRIter(15, 10);
			/////////////////////////////////////////
			

		}

		//modR()
		//performs modulo using recursion
		//receives: lefthand and righthand operands
		//returns: remainder
		uint modR(uint lh, uint rh)
		{
			//when lh or rh is zero
			//or when the modulus is actually 0
			//just return 0
			if (lh == 0)
				return 0;
			else if (rh == 0)
				return 0;
			else if (rh == lh)
				return 0;

			//if the numerator is less than the divisor
			//then it is the remainder
			else if (lh < rh)
				return lh;

			//otherwise, make a recursive call using lh-rh as the next numerator
			else
				return modR(lh - rh, rh);
				
		}

		//modD()
		//performs modulo using the division operator
		//receives: lefthand and righthand operands
		//returns: remainder
		uint modD(uint lh, uint rh)
		{
			//when lh or rh is zero
			//or when the modulus is actually 0
			//just return 0
			if (lh == 0)
				return 0;
			else if (rh == 0)
				return 0;
			else if (rh == lh)
				return 0;

			//if the numerator is less than the divisor
			//then it is the remainder
			else if (lh < rh)
				return lh;

			//otherwise, do some math using the built in arithmetic operators
			else
				return lh - (rh * (lh/rh));
		}

		//modB()
		//performs modulus using bitwise operations and no division
		//receives: lefthand and righthand operands
		//returns: remainder
		uint modB(uint lh, uint rh)
		{
			//when lh or rh is zero
			//or when the modulus is actually 0
			//just return 0
			if (lh == 0)
				return 0;
			else if (rh == 0)
				return 0;
			else if (rh == lh)
				return 0;

			//if the numerator is less than the divisor
			//then it is the remainder
			else if (lh < rh)
				return lh;

			else
			{
				uint remainder = lh; //temporary remainder that will eventually be the actual remainder
				uint multiple = 1; //multiple tracker

				//multiply the right operand and the multiple tracker by two 
				//using bit shift to the left by 1
				//until the right operand is greater than the left
				while (rh < lh)
				{
					rh = rh << 1;
					multiple = multiple << 1;
				}

				//divide the right operand and the multiple tracker by two
				//using bit shift to the right by 1
				//and set the remainder to the remainder - the right operand
				//until the multiple tracker is 0
				do
				{
					if (remainder >= rh)
					{
						remainder = remainder - rh;

					}
					rh = rh >> 1; // Divide by two.
					multiple = multiple >> 1;
				} while (multiple != 0);

				return remainder;
			}
		}

		//modO()
		//performs modulo division
		//using the built in mod operator
		//receives: left and right operands
		//returns: the remainder
		uint modO(uint lh, uint rh)
		{
			return lh % rh;
		}

		uint ModRIter(uint lh, uint rh)
		{
			uint result = 0;

			for(int i = 0; i < 10000; i++)
			{
				result = modR(lh, rh);
			}
			return result;
		}

        uint ModDIter(uint lh, uint rh)
        {
            uint result = 0;

            for (int i = 0; i < 10000; i++)
            {
                result = modD(lh, rh);
            }
            return result;
        }

        uint ModBIter(uint lh, uint rh)
        {
            uint result = 0;

            for (int i = 0; i < 10000; i++)
            {
                result = modB(lh, rh);
            }
            return result;
        }

        uint ModOIter(uint lh, uint rh)
        {
            uint result = 0;

            for (int i = 0; i < 10000; i++)
            {
                result = modO(lh, rh);
            }
            return result;
        }

    }

}
