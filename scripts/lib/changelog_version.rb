require_relative 'version'

class ChangelogVersion < Version
  VERSION_REGEX = %r{
    \A(?<year>\d{4})
    -(?<month>\d{2})
    -(?<day>\d{2})\z
  }x

  def year
    @year ||= extract_from_version(:year).to_i
  end
  alias_method :major, :year

  def month
    @month ||= extract_from_version(:month).to_i
  end
  alias_method :minor, :month

  def day
    @day ||= extract_from_version(:day).to_i
  end
  alias_method :patch, :day

  def to_s
    "%04d-%02d-%02d" % [year, month, day]
  end
end
