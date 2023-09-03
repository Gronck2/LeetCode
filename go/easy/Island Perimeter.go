package easy

func islandPerimeter(grid [][]int) int {
	perimetr := 0

	for i, row := range grid {
		for j, _ := range row {
			if grid[i][j] == 1 {
				perimetr += 4
				if i > 0 && grid[i-1][j] == 1 {
					perimetr -= 2
				}
				if j > 0 && grid[i][j-1] == 1 {
					perimetr -= 2
				}
			}
		}

	}

	return perimetr
}
