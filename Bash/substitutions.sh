convert image.{png,jpg}
# Will expand to
convert image.png image.jpg

cp /path/to/project/{foo,bar,baz}.sh /newpath
# Will expand to
cp /path/to/project/foo.sh /path/to/project/bar.sh /path/to/project/baz.sh /newpath

# Globbing techniques can also be combined
mv *{.py,.sh} folder
# Will move all *.py and *.sh files


mkdir foo bar
# This creates files foo/a, foo/b, ... foo/h, bar/a, bar/b, ... bar/h
touch {foo,bar}/{a..h}
touch foo/x bar/y

# Show differences between files in foo and bar, process substitution is used here
diff <(ls foo) <(ls bar)
# Outputs
# < x
# ---
# > y

echo "Starting program at $(date)" # Date will be substituted

echo "Running program $0 with $# arguments with pid $$"