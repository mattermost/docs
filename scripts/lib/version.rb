class Version < String
  VERSION_REGEX = %r{
    \A(?<year>\d{4})
    -(?<month>\d{2})
    -(?<day>\d{2})\z
  }x

  def <=>(other)
    return nil unless other.is_a?(Version)
    return 0 if self == other
    if year > other.year ||
        (year >= other.year && month > other.month) ||
        (year >= other.year && month >= other.month && day > other.day)
        1
    else
      -1
    end
  end

  def year
    @year ||= extract_from_version(:year).to_i
  end

  def month
    @month ||= extract_from_version(:month).to_i
  end

  def day
    @day ||= extract_from_version(:day).to_i
  end

  def version?
    self =~ self.class::VERSION_REGEX
  end

  def valid?
    self =~ self.class::VERSION_REGEX
  end

  def to_s
    "%04d-%02d-%02d" % [year, month, day]
  end

  private

  def extract_from_version(part, fallback: 0)
    match_data = self.class::VERSION_REGEX.match(self)
    if match_data && match_data.names.include?(part.to_s) && match_data[part]
      String.new(match_data[part])
    else
      fallback
    end
  end
end
