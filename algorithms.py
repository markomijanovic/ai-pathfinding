import random

import config



class Algorithm:
    def get_path(self, state):
        pass


class ExampleAlgorithm(Algorithm):
    def get_path(self, state):
        path = []
        while not state.is_goal_state():
            possible_actions = state.get_legal_actions()
            action = possible_actions[random.randint(0, len(possible_actions) - 1)]
            path.append(action)
            state = state.generate_successor_state(action)
        return path


class Blue(Algorithm):
    def get_path(self, state):
        visited = set()  # sva posjecena stanja
        stack = [(state, (), [])]
        while stack:
            curr_state, curr_action, curr_path = stack.pop(-1)
            curr_state_key = curr_state.get_state('S')
            if curr_state_key in visited:
                continue
            visited.add(curr_state_key)

            if curr_action:
                curr_path.append(curr_action)
            if curr_state.is_goal_state():
                return curr_path

            next_actions = reversed(curr_state.get_legal_actions())
            for action in next_actions:
                next_state = curr_state.generate_successor_state(action)
                next_state_key = next_state.get_state('S')  # provjeravamo da li je vec postojalo to stanje
                if next_state_key not in visited:
                    copy = curr_path.copy()
                    stack.append((next_state, action, copy))
        return None


class Red(Algorithm):
    def get_path(self, state):
        visited = set()
        queue = [(state, (), [])]
        while (len(queue)):
            curr_state, curr_action, curr_path = queue.pop(0)

            curr_state_key = curr_state.get_state('S')
            if curr_state_key in visited:
                continue

            visited.add(curr_state_key)

            if curr_action:
                curr_path.append(curr_action)
            if curr_state.is_goal_state():
                return curr_path
            next_actions = curr_state.get_legal_actions()
            for action in next_actions:
                next_state = curr_state.generate_successor_state(action)
                next_state_key = next_state.get_state('S')
                if next_state_key not in visited:
                    copy = curr_path.copy()
                    queue.append((next_state, action, copy))
        return None




class Black(Algorithm):
    def get_path(self, state):
        visited = dict()

        priority_queue = [(0, state, [])]  # (trosak, trenutno stanje, putanja)

        while priority_queue:
            cost, curr_state, curr_path = priority_queue.pop(0)

            if curr_state.is_goal_state():

                return curr_path

            curr_key = curr_state.get_state('S')
            if curr_key in visited and visited[curr_key] <= cost:
                continue
            visited[curr_key] = cost

            next_actions = curr_state.get_legal_actions()

            for action in next_actions:
                next_state = curr_state.generate_successor_state(action)
                action_cost = curr_state.get_action_cost(action)
                total_cost = cost + action_cost

                next_key = next_state.get_state('S')
                if next_key not in visited or total_cost < visited[next_key]:
                    new_path = curr_path + [action]
                    priority_queue.append((total_cost, next_state, new_path))
                    priority_queue.sort(key=lambda x: x[0])



        return None


def calculate_manhattan_heuristic(state):
    total_distance = 0
    spaceships = state.get_state('S')
    goals = state.get_state('G')

    spaceship_positions = decode_positions(spaceships)
    goal_positions = decode_positions(goals)

    for spaceship in spaceship_positions:

        min_distance = 1000
        closest_goal = None
        for goal in goal_positions:
            distance = abs(spaceship[0] - goal[0]) + abs(spaceship[1] - goal[1])
            if distance < min_distance:
                min_distance = distance
                closest_goal = goal

        total_distance += min_distance

        if closest_goal:
            goal_positions.remove(closest_goal)

    return total_distance

def decode_positions(bitmask):
    #Pretvara bitmasku u listu pozicija (x, y) gdje su '1' bitske vrijednosti u maski.
    positions = []
    bit_index = (config.M * config.N) - 1
    while bitmask:
        if bitmask & 1:
            row = bit_index // config.N
            col = bit_index % config.N
            positions.append((row, col))
        bitmask >>= 1
        bit_index -= 1
    return positions


class White(Algorithm):
    def get_path(self, state):
        visited = {}


        priority_queue = [(0, 0, state, [])]  # (total cost with heuristics, actual cost, state, path)

        while priority_queue:
            heu_cost, cost, curr_state, curr_path = priority_queue.pop(0)
            if curr_state.is_goal_state():
                return curr_path

            curr_key = curr_state.get_state('S')
            if curr_key in visited and visited[curr_key] <= heu_cost:
                continue
            visited[curr_key] = heu_cost
            next_actions = curr_state.get_legal_actions()

            for action in next_actions:
                next_state = curr_state.generate_successor_state(action)
                action_cost = curr_state.get_action_cost(action)
                cost_without_heuristic = cost + action_cost
                new_heu_cost = calculate_manhattan_heuristic(next_state)

                total_cost_with_heuristic = new_heu_cost + cost_without_heuristic
                next_key = next_state.get_state('S')


                if next_key not in visited or total_cost_with_heuristic < visited[next_key]:
                    new_path = curr_path + [action]
                    priority_queue.append((total_cost_with_heuristic, cost_without_heuristic, next_state, new_path))
                    priority_queue.sort(key=lambda x: x[0])


        return None
