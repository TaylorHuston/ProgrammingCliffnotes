require "minitest/autorun" #Part of the ruby standard library

class ExampleTest < Minitest::Test
  def test_truth
    assert true
  end
end

class Bacon
  def self.saved?
    false
  end
end

class BaconTest < Minitest::Test
  def test_saved
    assert Bacon.saved?, "Our bacon was not saved :(" #Failure error message
  end
end
