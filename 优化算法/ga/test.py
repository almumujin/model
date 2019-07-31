import copy
import random


class DNA:
    genes = ''
    fitness = 0

    def __init__(self):
        for i in range(genes_len):
            self.genes = self.genes + list(target)[random.randint(0, genes_len-1)]

    def cal_fitness(self):
        score = 0
        for i in range(genes_len):
            if list(self.genes)[i] == target[i]:
                score += 1
        self.fitness = float(score/len(target))

    def mutate(self):

        for i in range(genes_len):
            if random.random() < mutation_rate:
                list(self.genes)[i] = target[i]

    def crossover(self, partner):
        midpoint = []
        for i in range(random.randint(0, genes_len/2)):
            midpoint.append(random.randint(0, genes_len))
        for i in range(genes_len):
            if i in midpoint:
                # print(self.genes[i], partner.genes[i])
                temp = list(self.genes)[i]
                list(self.genes)[i] = list(partner.genes)[i]
                list(partner.genes)[i] = temp
        return self


def draw(mating_pool):
    tmp = []
    for i in range(len(mating_pool)):
        print(mating_pool[i].genes, mating_pool[i].fitness)
    for i in range(len(mating_pool)):
        mating_pool[i].cal_fitness()
    for i in range(len(mating_pool)):
        n = mating_pool[i].fitness * 100
        if n > 10:
            for i in range(int(n)):
                tmp.append(mating_pool[i])

    # 繁殖
    for i in range(len(tmp)):
        partnerA, partnerB = random.sample(tmp, 2)
        # print(partnerA.genes)
        child = partnerA.crossover(partnerB)
        child.mutate()
        tmp[i] = child
        # print(population[i].genes)

    mating_pool = copy.deepcopy(tmp)


if __name__ == '__main__':
    genes_len = 18
    population_len = 100
    target = "to be or not to be"
    mutation_rate = 0.2  # 突变概率
    total_population = 10
    mating_pool = []
    for i in range(population_len):
        mating_pool.append(DNA())
    for i in range(total_population):
        print(f"第{i}代--------------------------种群个数为{len(mating_pool)}")
        draw(mating_pool)

    # test = DNA()
    # test.cal_fitness()
    # print(test.fitness, test.genes)

