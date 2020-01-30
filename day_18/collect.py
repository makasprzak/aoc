from day_18.tree import Branch
from copy import deepcopy, copy
from itertools import permutations

class Collector:
    def __init__(self, steps: int, keys: dict, level=0):
        self.level = level
        self.steps = steps
        self.keys = keys
        self.closed = dict()
        self.completed = False
        self.last_key_at = 0
        self.last_distance = 0



def collect(branch: Branch, orig_collector: Collector):
    collector = deepcopy(orig_collector)
    picked_keys = dict()
    closed_doors = dict()
    items = list(branch.items.items())
    items.sort(key=lambda i: i[1])
    for item, distance in items:
        if ord(item) in range(ord('a'), ord('z')):
            picked_keys[item] = distance
        elif ord(item) in range(ord('A'), ord('Z')) and item.lower() not in picked_keys.keys() and item.lower() not in collector.keys.keys():
            closed_doors[item] = distance
            break

    if len(closed_doors) > 0:
        first_closed_door = list(closed_doors.items())[0]
        collector.keys.update(picked_keys)
        collector.last_key_at = last_key(picked_keys)[1] if len(picked_keys) > 0 else 0
        collector.steps += max(picked_keys.values()) if len(picked_keys) > 0 else 0
        collector.closed[first_closed_door] = branch
        return collector
    else:
        picked_keys = picked_keys
        collector.keys.update(picked_keys)
        collector.last_key_at = last_key(picked_keys)[1] if len(picked_keys) > 0 else 0
        collector.steps += max(picked_keys.values()) if len(picked_keys) > 0 else branch.steps
        if len(branch.children) == 0:

            print("Reached leaf at level: " + str(collector.level) + " going up")

            collector.completed = True
            collector.last_distance = branch.distance() + collector.last_key_at
            return collector
        else:
            min_steps = 1000000000
            best_collector = collector
            perms = permutations(list(branch.children.values()) + [None])
            # perms = filter(lambda p: p[0] is not None, set(map(slice_permutation, perms)))
            perms = set(map(slice_permutation, perms))
            for children in perms:
                print('########################################################################################')
                print('level {0} branch {1} trying permutation: '.format(collector.level, str(branch.direction)), list(map(lambda b: str(b.direction) if b is not None else "go_back", children)))
                print('########################################################################################')
                collected = try_permutation(branch, children, collector)
                if collected.completed and collected.last_key_at < min_steps:
                    min_steps = collected.last_key_at
                    best_collector = collected
            print("Best permutation: ", best_collector.last_key_at)
            return best_collector

def slice_permutation(perm: []):
    out = []
    for p in perm:
        out.append(p)
        if p is None:
            break
    return tuple(out)

def try_permutation(branch, children, collector):
    collector = deepcopy(collector)
    last_key_at = 0
    unblocked = children
    while len(unblocked) > 0:
        for child in unblocked:
            if child is None:
                break
            new_collector = Collector(branch.steps, collector.keys, level=collector.level + 1)
            collected = collect(child, new_collector)
            if not collected.completed:
                print("Closed door {0} at level {1}, direction: {2}".format(collected.closed.keys(), collected.level,
                                                                            str(child.direction)))
                collector.closed.update(collected.closed)
            if len(collected.keys) > 0:
                print("Collected {0} at level {1}, direction: {2}".format(collected.keys, collected.level,
                                                                          str(child.direction)))
                print("Therefore updating steps by: ", collected.last_key_at + branch.steps)
                last_key_at += collected.last_key_at + branch.steps
                collector.keys.update(collected.keys)
                collector.last_distance = collected.last_distance
        unblocked = []
        for k, v in list(collector.closed.items()).copy():
            if k[0].lower() in collector.keys.keys():
                collector.closed.pop(k)
                unblocked.append(v)
    if len(collector.closed) == 0:
        collector.completed = True
        collector.last_key_at += last_key_at + branch.steps
        return collector
    else:
        return collector


def first_door(door: dict):
    door_items = list(door.items())
    door_items.sort(key=lambda d: d[1])
    return door_items[0]

def last_key(keys: dict):
    key_items = list(keys.items())
    key_items.sort(key=lambda k: k[1], reverse=True)
    return key_items[0]
