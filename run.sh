function run {
	long_regex=".*L.*"

	[[ $1 =~ $long_regex ]]
	match=${BASH_REMATCH[0]}

	if [ "$match" = "$1" ]; then
		echo -n "!Note! The solution for ($1) might take some time, continue? (y/[n]): " 
		read response
		
		if [ "$response" = "y" ]; then
			if ["$2" = "1" ]; then
				`which python` $1 >> solutions
			else
				`which python` $1
			fi
		fi
	else
		if [ "$2" = "1" ]; then
			`which python` $1 >> solutions
		else
			`which python` $1
		fi
	
	fi
}

function new {
	echo -e "import helpers\n\nDAY = $1\nPART = 1\n\ndef solution(f_obj):\n\tpass" > day$1_pt1.py
	echo -e "\nhelpers.solve(DAY,PART,solution,line_by_line=True)\n" >> day$1_pt1.py

	echo -e "import helpers\n\nDAY = $1\nPART = 2\n\ndef solution(f_obj):\n\tpass" > day$1_pt2.py
	echo -e "\nhelpers.solve(DAY,PART,solution,line_by_line=True)\n" >> day$1_pt2.py
	
	touch day$1.txt;
}

optarg=$1
store=$2
scripts=$( find . -path "./day*.py" | sort -V ) 
last_edited=$( ls --sort=time | grep "day.*.py" | head -1 )
last_day=$( find . -path "./day*.py" | sort -V | tail -1 )
day_regex=".*day([0-9]{1,3})_.*"

if [ "$optarg" = "all" ]; then
	for s in $scripts; do
		run $s $store;
	done
fi

if [ "$optarg" = "last" ]; then
	run $last_edited;
fi

if [ "$optarg" = "new_day" ]; then
	[[ $last_day =~ $day_regex ]]
	day=`expr ${BASH_REMATCH[1]} + 1`;
	new $day;
fi

