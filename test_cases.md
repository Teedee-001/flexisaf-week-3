# Campus Utility Desk — Test Cases

| No. | Feature              | Test Input                       | Expected Result                                 |
| --- | -------------------- | -------------------------------- | ----------------------------------------------- |
| 1   | Calculator           | 5 + 3                            | Displays 8                                      |
| 2   | Calculator           | 10 / 0                           | Displays a division-by-zero error               |
| 3   | Calculator           | Invalid operator `%`             | Displays an invalid operator message            |
| 4   | Unit Converter       | 10 kilometres to miles           | Displays approximately 6.214 miles              |
| 5   | Unit Converter       | Negative distance: -5            | Rejects the distance                            |
| 6   | Unit Converter       | Invalid choice: 5                | Displays an invalid selection message           |
| 7   | Study Sprint Checker | 30 minutes, moderate energy      | Displays a suitable study recommendation        |
| 8   | Study Sprint Checker | Enter letters instead of minutes | Requests a valid whole number                   |
| 9   | Main Menu            | Enter option 9                   | Displays an invalid choice message              |
| 10  | Exit                 | Enter option 4                   | Displays a goodbye message and ends the program |

## Testing Result

Record the actual result for each test after running it.

- Passed: The program behaved as expected.
- Failed: The program behaved differently from what was expected.
