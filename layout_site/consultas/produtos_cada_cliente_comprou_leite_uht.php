<html>
	<head>
	<title>Chupa Mundo</title>
	</head>

	<body bgcolor="white">
		<?php
			echo "connecting to db...";
			$link = pg_connect("dbname=latpro");
			echo "done";

			$result = pg_exec($link, "select id, a.cnpj, razao_social from cliente a, (select leite_uht.id, compra_leite_uht.cnpj from leite_uht, compra_leite_uht where leite_uht.id = compra_leite_uht.id) b where a.cnpj = b.cnpj");
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
					</tr>
					";
				}
				pg_close($link);
			?>
		</table>
	</body>
</html>
