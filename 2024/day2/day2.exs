defmodule Day2 do

  defp split_line_and_cast(line) do
    String.split(line, " ", trim: true)
    |> Enum.map(&(String.to_integer)/1)
  end

  def clean_input(filename) do
    {:ok, input} = File.read(filename)
    input
    |> String.split("\n", trim: true)
    |> Enum.map(&(split_line_and_cast)/1)
  end

  defp _diffs([]), do: []
  defp _diffs([ head | [ next | tail]]) when length(tail) == 0 do
    next - head
  end
  defp _diffs([ head | [ next | tail]]) do
    [ next - head, _diffs([next | tail]) ]
    |> List.flatten
  end

  defp _stable(diffs) do
    [increasing, decreasing] = [Enum.any?(diffs, &(&1 > 0)), Enum.any?(diffs, &(&1 < 0))]
    (increasing and not decreasing) or (decreasing and not increasing)
  end

  defp _safety_check(report) do
    diffs = _diffs(report)
    (not Enum.any?(diffs, &(abs(&1) == 0 or abs(&1) > 3))) and (_stable(diffs))
  end

  def could_be_safe(report) do
    idx = Enum.to_list(0..length(report))
    Stream.map(idx, fn i -> List.delete_at(report, i) end)
    |> Stream.map(&(_safety_check)/1)
    |> Enum.any?
  end

  def dampened_safety_check(reports) do
    reports
    |> Stream.reject(&(_safety_check)/1)
    |> Stream.filter(&(could_be_safe)/1)
    |> Enum.to_list
    |> Enum.count
  end

  def safety_check(reports) do
    reports
    |> Stream.filter(&(_safety_check)/1)
    |> Enum.to_list
    |> Enum.count
  end
end

# safe = Day2.clean_input("input.txt") |> Day2.safety_check
# dampened = Day2.clean_input("input.txt") |> Day2.dampened_safety_check
# safe + dampened
