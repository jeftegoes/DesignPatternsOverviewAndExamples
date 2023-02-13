from database import Database


class SingletonRecordFinder:
    def total_population(self, cities):
        result = 0
        for c in cities:
            result += Database().population[c]
        return result
