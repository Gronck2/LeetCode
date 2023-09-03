package easy

func convertToTitle(columnNumber int) string {
	title := ""
	for columnNumber > 0 {
		digit := (columnNumber - 1) % 26
		title = string('A'+digit) + title
		columnNumber = (columnNumber - 1) / 26
	}

	return title
}
