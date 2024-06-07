<?
header("FLAG-PART-2: \"4N_1nspeCT\" (hint: see the source by /?now-you-see-me");

if (isset($_GET["now-you-see-me"])) {
	highlight_file(__file__);
}

$FLAG_PART_3 = "_eLemEnT";

// TODO: for god damn, please rename the fan-page-club88213.html to something better :(
?>

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Inspect Element Fans</title>
	<!-- they won't see this one: MOTORI{1am_ -->
	<!-- for part two (hint1: check the response headers) -->
</head>
<body>
	<h1>Hello ctf player</h1>
	<p>To find the flag you need to find four part of flag</p>
	<span>just follow the title</span>
</body>
</html>