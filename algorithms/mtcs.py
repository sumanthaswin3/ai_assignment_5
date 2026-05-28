import random

    def uct(self):
        if self.visits == 0:
            return float('inf')

        return (self.wins / self.visits) + math.sqrt(
            2 * math.log(self.parent.visits) / self.visits
        )


class SimpleGame:
    def get_moves(self, state):
        return [1, 2, 3]

    def next_state(self, state, move):
        return state + move

    def is_terminal(self, state):
        return state >= 10

    def reward(self, state):
        return 1 if state % 2 == 0 else 0


class MCTS:
    def __init__(self, game):
        self.game = game

    def search(self, initial_state, iterations=1000):
        root = Node(initial_state)

        for _ in range(iterations):
            node = root
            state = initial_state

            while node.children:
                node = max(node.children, key=lambda n: n.uct())
                state = node.state

            if not self.game.is_terminal(state):
                for move in self.game.get_moves(state):
                    new_state = self.game.next_state(state, move)
                    child = Node(new_state, node)
                    node.children.append(child)

                node = random.choice(node.children)
                state = node.state

            while not self.game.is_terminal(state):
                move = random.choice(self.game.get_moves(state))
                state = self.game.next_state(state, move)

            reward = self.game.reward(state)

            while node:
                node.visits += 1
                node.wins += reward
                node = node.parent

        best_child = max(root.children, key=lambda n: n.visits)
        return best_child.state


if __name__ == '__main__':
    game = SimpleGame()
    mcts = MCTS(game)

    best_state = mcts.search(0)
    print('Best State:', best_state)
