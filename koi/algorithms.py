from koi.participant import Participant
import random


class Algo:

    def __init__(self, data):
        # data is an array of Participant
        self.data = data
        self.size = len(data)

    def random_select(self):
        return random.choice(self.data)

    def filter_eligibility_select(self):
        data = list(filter(lambda participant: participant.eligibility == 1, self.data))
        return random.choice(data)

    def filter_credit_select(self, grid):

        tot = 0
        for credit in range(600, 1000, grid):
            tot += credit

        prob_map = {}
        probs = []
        prob = 0
        idx = 0
        for credit in range(600, 1000, grid):
            prob += credit / tot
            probs.append(prob)
            prob_map[idx] = credit
            idx += 1
        probs[-1] = 1.01

        temp_data = list(filter(lambda participant: participant.eligibility == 1 and participant.credit >= 600,
                                self.data))

        random_prob = random.random()
        print(random_prob)

        ptr = 0
        while random_prob > probs[ptr]:
            ptr += 1

        data = list(filter(
            lambda participant: prob_map[ptr] <= participant.credit < prob_map[ptr] + grid,
            temp_data))

        if not data:
            return self.filter_credit_select(grid)

        return random.choice(data)


# create participants
# p1 = Participant("Alex", 15, "", "", 1)
# p2 = Participant("Alex", 15, "", "", 1)
# p3 = Participant("Alex", 15, "", "", 1)

# create a group
group_1 = [Participant("Person" + str(i), random.randint(15, 40), random.randint(350, 950), "", random.randint(0, 1)) for i in range(1000000)]

algo = Algo(group_1)

# iter_1 = 5
# print("\n" + "Select " + str(iter_1) + " person randomly")
# for _ in range(iter_1):
#     chosen_person = algo.random_select()
#     print(chosen_person.name + " with eligibility: " + str(chosen_person.eligibility))
#
# iter_2 = 5
# print("\n" + "Select " + str(iter_2) + " person randomly, only select those who are eligible")
# for _ in range(iter_2):
#     chosen_person = algo.filter_eligibility_select()
#     print(chosen_person.name + " with eligibility: " + str(chosen_person.eligibility))
#
# iter_3 = 5
# print("\n" + "Select " + str(iter_3) + " person randomly, only select those who have enough credits")
# for _ in range(iter_3):
#     chosen_person = algo.filter_credit_select(1)
#     print(chosen_person.name + " with eligibility: " + str(chosen_person.eligibility) + ", with credit: " +
#           str(chosen_person.credit))


iter_4 = 100
tot_chosen_person_credit = 0
for _ in range(iter_4):
    tot_chosen_person_credit += algo.filter_credit_select(1).credit
print(tot_chosen_person_credit * 1.0 / iter_4)

