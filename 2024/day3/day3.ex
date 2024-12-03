defmodule Day3 do

  def mul("do()"), do: true
  def mul("don't()"), do: false
  def mul(op) do
    [a, b] = cast(op)
    a * b
  end

  def conditional_sum([], _), do: 0
  def conditional_sum([false | tail], _), do: conditional_sum(tail, false)
  def conditional_sum([true | tail], _), do: conditional_sum(tail, true)
  def conditional_sum([head | tail], enabled) when enabled, do: head + conditional_sum(tail, enabled)
  def conditional_sum([_ | tail], enabled) when not enabled, do: 0 + conditional_sum(tail, enabled)

  def match_conditional_muls(line) do
    Regex.scan(~r"(do\(\))|(don't\(\))|(mul\([1-9][0-9]*,[1-9][0-9]*\))", line)
    |> Enum.map(fn [match | _ ] -> match end)
  end

  def match_muls(line) do
    Regex.scan(~r"mul\([1-9][0-9]*,[1-9][0-9]*\)", line)
    |> List.flatten
    |> Enum.map(&cast/1)
  end

  def cast(match) do
    Regex.scan(~r"[1-9][0-9]*", match)
    |> List.flatten
    |> Enum.map(&(String.to_integer(&1)/1))
  end

  def stream_input(filename) do
    File.stream!(filename)
    |> Stream.map(&match_conditional_muls/1)
    |> Enum.concat
    |> Enum.map(&mul/1)
    |> conditional_sum(true)
  end

end
