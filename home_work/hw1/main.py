# -*- coding: utf-8 -*-
# initializing empty envelops

necessityEnvelop = 0  # NEC, необхідні витрати
freedomEnvelop = 0  # FFA, фінансова свобода
educationEnvelop = 0  # EDU, освіта
longTermEnvelop = 0  # LTSS, резерв та на великі покупки
playEnvelop = 0  # PLAY, розваги
giveEnvelop = 0  # GIVE, подарунки

# initializing percent rate
necRate = 0.55
ffaRate = 0.1
eduRate = 0.1
ltssRate = 0.1
playRate = 0.1
giveRate = 0.05
# initializing expected income, expected necessity and other amounts
expectedIncome = 1000

# invitation, greetings etc.
print(f"Hello.\n"
      f"We gonna fill your envelops by the money you input here!\n"
      f"Please input your amounts of money income and see the results.\n"
      f"Press Ctrl+c to exit script."
      f"\n\n Enter the amount please:")

# initializing handler for standard input
sum = 0

while (sum < expectedIncome):
    line = int(input())
    sum += line

    necessityEnvelop += line * necRate
    freedomEnvelop += line * ffaRate
    educationEnvelop += line * eduRate
    longTermEnvelop += line * ltssRate
    playEnvelop += line * playRate
    giveEnvelop += line * giveRate

    print(f"\n Enter the amount please:")

# final output
print(f"At the end we have:\n"
      f"Necessity Envelop has:                        {str(int(necessityEnvelop))} \n"
      f"Financial Freedom Envelop has:                {str(int(freedomEnvelop))} \n"
      f"Education Envelop                             {str(int(educationEnvelop))} \n"
      f"Long Term Saving for Spending Envelop has:    {str(int(longTermEnvelop))} \n"
      f"Play Envelop has:                             {str(int(playEnvelop))} \n"
      f"Give Envelop has:                             {str(int(giveEnvelop))} \n"
      f"{'_' * 70} \n\n"
      f"Thanks for using our software :)")
