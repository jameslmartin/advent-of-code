defmodule Day1 do
  defp transpose(rows) do
    rows
    |> List.zip
    |> Enum.map(&Tuple.to_list/1)
  end

  def clean_input(file) do
    {:ok, input} = File.read(file)
    input
    |> String.split("\n", trim: true)
    |> Enum.map(&(String.split(&1, " ", trim: true)))
    |> transpose
  end

  def sort_diff_and_sum([l1, l2]) do
    Enum.zip_with([Enum.sort(l2), Enum.sort(l1)], fn [x, y] -> abs(String.to_integer(y) - String.to_integer(x)) end)
    |> Enum.sum
  end

  def similarity_score([left, right]) do
    Enum.map(left, fn l -> String.to_integer(l) * Enum.count(right, &(&1 == l)) end)
    |> Enum.sum
  end
end
