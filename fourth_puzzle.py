def wordsearch(grid):
    m = len(grid)
    n = len(grid[0])
    def dfs(i, j, word, dir):
        if len(word) == 0:
            return 1
        if i < 0 or j < 0 or i >= m or j >= n:
            return 0
        
        if grid[i][j] != word[0]:
            return 0
        
        return dfs(i + dir[0], j + dir[1], word[1:], dir)
        
    nb_found = 0
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'X':
                nb_found += dfs(i, j+1, "MAS", (0, 1))
                nb_found += dfs(i+1, j+1, "MAS", (1, 1))
                nb_found += dfs(i+1, j, "MAS", (1, 0))
                nb_found += dfs(i+1, j-1, "MAS", (1, -1))
                nb_found += dfs(i, j-1, "MAS", (0, -1))
                nb_found += dfs(i-1, j-1, "MAS", (-1, -1))
                nb_found += dfs(i-1, j, "MAS", (-1, 0))
                nb_found += dfs(i-1, j+1, "MAS", (-1, 1))

    return nb_found

def wordsearch_part_two(grid):
    m = len(grid)
    n = len(grid[0])
        
    nb_found = 0
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'A':
                if i-1 < 0 or j-1 < 0 or i+1 >= m or j+1 >= n:
                    continue
                first_diagonal = (grid[i-1][j-1] == 'M' and grid[i+1][j+1] == 'S') or (grid[i-1][j-1] == 'S' and grid[i+1][j+1] == 'M')
                second_diagonal = (grid[i+1][j-1] == 'M' and grid[i-1][j+1] == 'S') or (grid[i+1][j-1] == 'S' and grid[i-1][j+1] == 'M')

                nb_found += (first_diagonal & second_diagonal)

    return nb_found

def main():
    # Input parsing
    with open("data/input_4.txt") as f:
        grid = []
        for line in f:
            parsed_line = line[:-1] if line[-1] == '\n' else line
            grid.append(list(parsed_line))
            

    print(wordsearch_part_two(grid))


if __name__ == "__main__":
    main()