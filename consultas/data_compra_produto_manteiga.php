<html>
	<head>
	<title>Chupa Mundo</title>
	</head>

	<body bgcolor="white">
		<?php
			echo "connecting to db...";
			$link = pg_connect("dbname=latpro");
			echo "done";

			$result = pg_exec($link, "select id, a.cnpj, razao_social, data from cliente a, (select manteiga.id, compra_manteiga.cnpj, compra_manteiga.data from manteiga, compra_manteiga where manteiga.id = compra_manteiga.id) b where a.cnpj = b.cnpj");
			$numrows = pg_numrows($result);

			//echo "<p>link = $link<br>
			//result = $result<br>
			//numrows = $numrows</p>
		?>

		<table border="1">
			<tr>
				<th>id</th>
				<th>cnpj</th>
				<th>razao social</th>
				<th>data_compra_manteiga</th>
			</tr>

			<?php
				//loop on rows in the result set.
				for($ri = 0; $ri < $numrows; $ri++) {
					echo "<tr>\n";
					$row = pg_fetch_array($result, $ri);
					echo 
					"<td>", $row["id"], "</td>
					<td>", $row["cnpj"], "</td>
					<td>", $row["razao_social"], "</td>
					<td>", $row["data"], "</td>
					</tr>
					";
				}
				pg_close($link);
			?>
		</table>
	</body>
</html>
