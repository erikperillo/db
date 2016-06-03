<html>
	<head>
	<title>Chupa Mundo</title>
	</head>

	<body bgcolor="white">
		<?php
			echo "connecting to db...";
			$link = pg_connect("dbname=latpro");
			echo "done";

			$result = pg_exec($link, "select preco, cnpj from insumo");
			$numrows = pg_numrows($result);

			//echo "<p>link = $link<br>
			//result = $result<br>
			//numrows = $numrows</p>
		?>

		<table border="1">
			<tr>
				<th>preco</th>
				<th>cnpj</th>
			</tr>

			<?php
				//loop on rows in the result set.
				for($ri = 0; $ri < $numrows; $ri++) {
					echo "<tr>\n";
					$row = pg_fetch_array($result, $ri);
					echo 
					"<td>", $row["preco"], "</td>
					<td>", $row["cnpj"], "</td>
					</tr>
					";
				}
				pg_close($link);
			?>
		</table>
	</body>
</html>
