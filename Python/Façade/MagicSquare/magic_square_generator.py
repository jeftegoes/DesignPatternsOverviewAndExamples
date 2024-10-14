from generator import Generator
from splitter import Splitter
from verifier import Verifier


class MagicSquareGenerator:
    def generate(self, size: int):
        generator = Generator()
        splitter = Splitter()
        verifier = Verifier()

        while True:
            square = []
            for x in range(size):
                square.append(generator.generate(size))

            print(square)

            if verifier.verify(splitter.split(square)):
                break

        return square
