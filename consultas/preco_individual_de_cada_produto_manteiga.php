<html>
	<head>
	<title>Chupa Mundo</title>
	</head>

	<body bgcolor="white">
		<?php
			echo "connecting to db...";
			$link = pg_connect("dbname=latpro");
			echo "done";

			$result = pg_exec($link, "select id, preco_manteiga from manteiga");
			$numrows = pg_numrows($result);

			//echo "<p>link = $link<br>
			//result = $result<br>
			//numrows = $numrows</p>
		?>

		<table border="1">
			<tr>
				<th>id</th>
				<th>preco_manteiga</th>
			</tr>

			<?php
				//loop on rows in the result set.
				for($ri = 0; $ri < $numrows; $ri++) {
					echo "<tr>\n";
					$row = pg_fetch_array($result, $ri);
					echo 
					"<td>", $row["id"], "</td>
					<td>", $row["preco_manteiga"], "</td>
					</tr>
					";
				}
				pg_close($link);
			?>
		</table>
	</body>
</html>
