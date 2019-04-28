--
-- Editor SQL for DB table graphs
-- Created by http://editor.datatables.net/generator
--

CREATE TABLE IF NOT EXISTS graphs (
	id serial,
	node_count integer,
	edge_count integer,
	diameter integer,
	total_edge_cost integer,

	convergence_rate numeric(9,2),
	energy_cost numeric(9,2),
	eccentricity_average numeric(9,2),

	PRIMARY KEY( id )
);

CREATE TABLE IF NOT EXISTS node_structure (
	id serial,
	graph_id integer,
	nodes text,

	PRIMARY KEY( id )
);

CREATE TABLE IF NOT EXISTS edge_structure (
	id serial,
	graph_id integer,
	edges text,

	PRIMARY KEY( id )
);

CREATE TABLE IF NOT EXISTS eccentricity_distribution (
	id serial,
	graph_id integer,
	eccentricity text,

	PRIMARY KEY( id )
);