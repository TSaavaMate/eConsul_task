class TowerOfHanoi:

    def __init__(self, discs, source, auxiliary, target):
        if not discs:
            raise ValueError("discs must be greater than 0")
        self.__discs = discs
        self.__source = source
        self.__middle = auxiliary
        self.__target = target

    @staticmethod
    def move_disc(from_peg: str, to_peg: str, disc: int) -> None:
        print(f"Move disc {disc} from {from_peg} to {to_peg}")

    def solve(self) -> None:
        self.__arrange_tower(self.__discs, self.__source, self.__target, self.__middle)

    def __arrange_tower(self, discs: int, source: str, target: str, middle: str):
        # Base case: If there's only one disc left, move it directly from source to target.
        if discs == 1:
            self.move_disc(source, target, 1)
            return

        # case 2 if there is more than 1 disc:
        # Moving (discs - 1) discs from source to middle,help of the target peg .
        self.__arrange_tower(discs - 1, source, middle, target)

        # Moving the largest disc from the source to the target .
        self.move_disc(source, target, discs)

        # Move the remaining (discs - 1) discs from the middle to the target help of source peg
        self.__arrange_tower(discs - 1, middle, target, source)

    def increase_discs(self):
        self.__discs += 1


hanoi = TowerOfHanoi(3, "A", "B", "C")
hanoi.solve()
