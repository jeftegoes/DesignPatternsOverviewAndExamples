namespace Facade
{
    public class Splitter
    {
        public List<List<int>> Split(List<List<int>> array)
        {
            var result = new List<List<int>>();

            var rowCount = array.Count;
            var colCount = array[0].Count;

            GetRows(array, result, rowCount, colCount);

            GetColumns(array, result, rowCount, colCount);

            var diag1 = new List<int>();
            var diag2 = new List<int>();

            GetDiagonals(array, rowCount, colCount, diag1, diag2);

            result.Add(diag1);
            result.Add(diag2);

            return result;
        }

        private void GetDiagonals(List<List<int>> array, int rowCount, int colCount, List<int> diag1, List<int> diag2)
        {
            for (int c = 0; c < colCount; ++c)
            {
                for (int r = 0; r < rowCount; ++r)
                {
                    if (c == r)
                        diag1.Add(array[r][c]);
                    var r2 = rowCount - r - 1;
                    if (c == r2)
                        diag2.Add(array[r][c]);
                }
            }
        }

        private void GetColumns(List<List<int>> array, List<List<int>> result, int rowCount, int colCount)
        {
            for (int c = 0; c < colCount; ++c)
            {
                var theCol = new List<int>();
                for (int r = 0; r < rowCount; ++r)
                    theCol.Add(array[r][c]);

                result.Add(theCol);
            }
        }

        private void GetRows(List<List<int>> array, List<List<int>> result, int rowCount, int colCount)
        {
            for (int r = 0; r < rowCount; ++r)
            {
                var theRow = new List<int>();
                for (int c = 0; c < colCount; ++c)
                    theRow.Add(array[r][c]);

                result.Add(theRow);
            }
        }
    }
}