#A very simple implementation of the BFS algorithm used to solve mazes, that consist of # - walls and Starts "S"
#and ends "E". The algorithm does not check if the maze is complete in terms of not holes in the walls - that leads to crash
#We use backtracking to reconstruct the shortest path

import sys

class labyrinth():
    #Innit and load the labyrinth and find start
    def __init__(self, path):
        self.finalPath = [];
        self.labyr = [];
        file = open(path);
        line = file.readline();
        while (len(line) > 0):
            self.labyr.append(line);
            line = file.readline();
        for i in self.labyr:
            if ("S" in i):
                self.start = (i.index("S"), self.labyr.index(i));
        file.close();
    #Return char at the given coordinates from the arrays
    def returnAt(self, coord):
        return self.labyr[coord[1]][coord[0]];
    #Use BFS to search trough array, print if the maze is not solvable
    def search(self):
        queue = [self.start];
        visited = [];
        backtrack = {};
        while (len(queue) > 0):
            current = queue.pop(0);
            if (self.returnAt(current) == "E"):
                self.end = current;
                self.reconstructPath(current, backtrack);
                self.saveSolvedLabyrinth();
                return True;
            upper = (current[0], current[1] + 1);
            down = (current[0], current[1] - 1);
            right = (current[0] + 1, current[1]);
            left = (current[0] - 1, current[1]);
            if (self.returnAt(upper) != "#" and upper not in visited and upper):
                visited.append(upper);
                backtrack.update({upper : current});
                queue.append(upper);
            if (self.returnAt(down) != "#" and down not in visited):
                visited.append(down);
                backtrack.update({down : current});
                queue.append(down);
            if (self.returnAt(right) != "#" and right not in visited):
                visited.append(right);
                backtrack.update({right : current});
                queue.append(right);
            if (self.returnAt(left) != "#" and left not in visited):
                visited.append(left);
                backtrack.update({left : current});
                queue.append(left);
        print("Not solvable");
    #Recursively reconstruct the path from the given dictionary and save it into the self.finalPath
    def reconstructPath(self, current, backtrack):
        if (current == labyr.start):
            return;
        self.finalPath.append(current);
        return self.reconstructPath(backtrack.get(current), backtrack);
    #Print the final outcome to stdout
    def printSolvedLabyrinth(self):
        for i in range (0, len(self.labyr)):
            for k in range(0, len(self.labyr[i])):
                #do not overprint the "E" letter
                if ((k, i) in self.finalPath and (k, i) != self.end):
                    print("*", end = "");
                    continue;
                print(self.labyr[i][k], end = "");
    #Save the solved labyrith into a file called "final"
    def saveSolvedLabyrinth(self):
        with open('final', 'w') as f:
            sys.stdout = f;
            for i in range (0, len(self.labyr)):
                for k in range(0, len(self.labyr[i])):
                    #do not overprint the "E" letter
                    if ((k, i) in self.finalPath and (k, i) != self.end):
                        print("*", end = "");
                        continue;
                    print(self.labyr[i][k], end = "");
        f.close();


labyr = labyrinth("./LabyrinthTests/labyrinth4");
labyr.search();

