defmodule Day1 do
  defp transpose(rows) do
    rows
    |> List.zip
    |> Enum.map(&Tuple.to_list/1)
  end

  defp to_lists(list) do
    Enum.map list, &(String.split(&1, " ", trim: true))
  end

  def clean_input(file) do
    {:ok, input} = File.read(file)
    input
    |> String.split("\n", trim: true)
    |> to_lists
    |> transpose
  end

  def sort_diff_and_sum([l1, l2]) do
    l1 = Enum.sort(l1)
    l2 = Enum.sort(l2)
    Enum.zip_with([l1, l2], fn [x, y] -> abs(String.to_integer(y) - String.to_integer(x)) end)
    |> Enum.sum
  end

  def similarity_score([left, right]) do
    Enum.map(left, fn l -> String.to_integer(l) * Enum.count(right, &(&1 == l)) end)
    |> Enum.sum
  end
end
