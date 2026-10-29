<?php
/**
 * Plugin Name: SJ Academy brand stylesheet
 * Description: Loads sj-brand.min.css on every front-end page. Must-use plugin: survives theme changes and cannot be deactivated from the dashboard.
 * Version: 1.0
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }

add_action( 'wp_enqueue_scripts', function () {
	$file = WPMU_PLUGIN_DIR . '/sj-brand/sj-brand.min.css';
	if ( ! file_exists( $file ) ) { return; }
	wp_enqueue_style(
		'sj-brand',
		WPMU_PLUGIN_URL . '/sj-brand/sj-brand.min.css',
		array(),
		filemtime( $file ) // new file = new version number = browsers and caches fetch the new copy
	);
}, 999 );
